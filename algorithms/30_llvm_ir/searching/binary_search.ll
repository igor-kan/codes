; ModuleID = 'algorithms/02_c/searching/binary_search.c'
source_filename = "algorithms/02_c/searching/binary_search.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [52 x i8] c"[C BinarySearch] lower_bound / upper_bound verified\00", align 1
@str.3 = private unnamed_addr constant [37 x i8] c"[C BinarySearch] FAILED: upper_bound\00", align 1
@str.4 = private unnamed_addr constant [37 x i8] c"[C BinarySearch] FAILED: lower_bound\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local range(i32 0, 1073741825) i32 @lower_bound(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = icmp sgt i32 %1, 0
  br i1 %4, label %5, label %18

5:                                                ; preds = %3, %5
  %6 = phi i32 [ %16, %5 ], [ 0, %3 ]
  %7 = phi i32 [ %15, %5 ], [ %1, %3 ]
  %8 = add nuw nsw i32 %6, %7
  %9 = lshr i32 %8, 1
  %10 = zext nneg i32 %9 to i64
  %11 = getelementptr inbounds nuw i32, ptr %0, i64 %10
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = icmp slt i32 %12, %2
  %14 = add nuw nsw i32 %9, 1
  %15 = select i1 %13, i32 %7, i32 %9
  %16 = select i1 %13, i32 %14, i32 %6
  %17 = icmp slt i32 %16, %15
  br i1 %17, label %5, label %18, !llvm.loop !9

18:                                               ; preds = %5, %3
  %19 = phi i32 [ 0, %3 ], [ %16, %5 ]
  ret i32 %19
}

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local range(i32 0, 1073741825) i32 @upper_bound(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = icmp sgt i32 %1, 0
  br i1 %4, label %5, label %18

5:                                                ; preds = %3, %5
  %6 = phi i32 [ %16, %5 ], [ 0, %3 ]
  %7 = phi i32 [ %15, %5 ], [ %1, %3 ]
  %8 = add nuw nsw i32 %6, %7
  %9 = lshr i32 %8, 1
  %10 = zext nneg i32 %9 to i64
  %11 = getelementptr inbounds nuw i32, ptr %0, i64 %10
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = icmp sgt i32 %12, %2
  %14 = add nuw nsw i32 %9, 1
  %15 = select i1 %13, i32 %9, i32 %7
  %16 = select i1 %13, i32 %6, i32 %14
  %17 = icmp slt i32 %16, %15
  br i1 %17, label %5, label %18, !llvm.loop !11

18:                                               ; preds = %5, %3
  %19 = phi i32 [ 0, %3 ], [ %16, %5 ]
  ret i32 %19
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  br label %1

1:                                                ; preds = %1, %0
  %2 = phi i32 [ %8, %1 ], [ 0, %0 ]
  %3 = phi i32 [ %7, %1 ], [ 6, %0 ]
  %4 = add nuw nsw i32 %3, %2
  %5 = lshr i32 %4, 1
  %6 = icmp eq i32 %5, 0
  %7 = select i1 %6, i32 %3, i32 %5
  %8 = select i1 %6, i32 1, i32 %2
  %9 = icmp samesign ult i32 %8, %7
  br i1 %9, label %1, label %10, !llvm.loop !9

10:                                               ; preds = %1
  %11 = icmp eq i32 %8, 0
  br i1 %11, label %27, label %12

12:                                               ; preds = %10, %12
  %13 = phi i32 [ %21, %12 ], [ 0, %10 ]
  %14 = phi i32 [ %20, %12 ], [ 6, %10 ]
  %15 = add nuw nsw i32 %14, %13
  %16 = lshr i32 %15, 1
  %17 = and i32 %15, -4
  %18 = icmp eq i32 %17, 8
  %19 = add nuw nsw i32 %16, 1
  %20 = select i1 %18, i32 %16, i32 %14
  %21 = select i1 %18, i32 %13, i32 %19
  %22 = icmp slt i32 %21, %20
  br i1 %22, label %12, label %23, !llvm.loop !11

23:                                               ; preds = %12
  %24 = icmp ne i32 %21, 4
  %25 = select i1 %24, ptr @str.3, ptr @str
  %26 = zext i1 %24 to i32
  br label %27

27:                                               ; preds = %23, %10
  %28 = phi ptr [ %25, %23 ], [ @str.4, %10 ]
  %29 = phi i32 [ %26, %23 ], [ 1, %10 ]
  %30 = tail call i32 @puts(ptr nonnull dereferenceable(1) %28)
  ret i32 %29
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #2

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
