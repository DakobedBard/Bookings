import { NgModule } from '@angular/core';
import { MatToolbarModule,  
  MatIconModule,  
  MatCardModule,  
  MatButtonModule,  
  MatProgressBarModule,
  MatListModule,
  MatMenuModule,
  MatGridListModule,
  MatDividerModule,
  MatExpansionModule,
  MatFormFieldModule,
  MatProgressSpinnerModule,
  MatInputModule,
  MatTabsModule,
  MatSelectModule,
  MatCheckboxModule,
  MatDatepickerModule, 
  MatNativeDateModule 

  
} from '@angular/material';
import { MatBadgeModule} from '@angular/material/badge';
const MaterialsComponents = [
  MatButtonModule, 
  MatToolbarModule,  
  MatIconModule,  
  MatCardModule,
  MatProgressBarModule,
  MatBadgeModule,
  MatListModule,
  MatMenuModule,
  MatGridListModule,
  MatDividerModule,
  MatExpansionModule,
  MatFormFieldModule,
  MatProgressSpinnerModule,
  MatInputModule,
  MatTabsModule,
  MatSelectModule,
  MatCheckboxModule,
  MatDatepickerModule, 
  MatNativeDateModule 
];


@NgModule({

  imports: [MaterialsComponents],
  exports: [MaterialsComponents]
})
export class MaterialModule { }
